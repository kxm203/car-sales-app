import React, { useState, useEffect } from "react";
import NewMustangForm from "./NewMustangForm";
import MustangList from "./MustangList";
import Search from "./Search";


function MustangPage() {
    const [mustangs, setMustangs] = useState([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [filteredMustangs, setFilteredMustangs] = useState(mustangs);

    useEffect(() => {
        fetch("http://localhost:5555/mustangs")
        .then((resp) => resp.json())
        .then((data) => setMustangs(data))
    }, []);

    const addMustang = (newMustang) => {
        fetch("http://localhost:5555/mustangs", {
            method: "POST",
            headers: {"Content-Type": "Application/JSON"},
            body: JSON.stringify(newMustang),
        })
        .then((resp) => resp.json())
        .then((data) => {
            setMustangs([...mustangs, data]);
        })
    };
    useEffect(() => {
        const filtered = mustangs.filter((mustang) =>
        mustang.color.toLowerCase().includes(searchQuery.toLowerCase())
        );
        setFilteredMustangs(filtered);
        console.log(mustangs)
    }, [searchQuery, mustangs]);

    const handleSearch = (query) => {
        setSearchQuery(query);
    };

    const deleteMustang = (mustangId) => {
        fetch(`http://localhost:5555/mustangs/${mustangId}`, {
            method:"DELETE",
        })
        .then((resp) => {
            if (resp.ok) {
                setFilteredMustangs((originalMustangs) =>
                originalMustangs.filter((mustang) => mustang.id !== mustangId)
                );
            } else {
                console.error("Failed to delete Mustang");
            }
        });
    };

    return (
        <main>
            <NewMustangForm addMustang={addMustang}/>
            <Search onChange={handleSearch}/>
            <MustangList mustangs={filteredMustangs} deleteMustang={deleteMustang} addMustang={addMustang}/>
        </main>
    );
}

export default MustangPage;
