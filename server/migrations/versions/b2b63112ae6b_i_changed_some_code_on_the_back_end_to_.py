"""I changed some code on the back end to try and get Postman to work.

Revision ID: b2b63112ae6b
Revises: 1761c8f06ca1
Create Date: 2024-03-25 15:14:22.919581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2b63112ae6b'
down_revision = '1761c8f06ca1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ford_mustang_bid_association',
    sa.Column('ford_mustang_id', sa.Integer(), nullable=True),
    sa.Column('bid_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bid_id'], ['bids.id'], name=op.f('fk_ford_mustang_bid_association_bid_id_bids')),
    sa.ForeignKeyConstraint(['ford_mustang_id'], ['ford_mustangs.id'], name=op.f('fk_ford_mustang_bid_association_ford_mustang_id_ford_mustangs'))
    )
    op.drop_table('ford_mustang_bid_asscoiation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ford_mustang_bid_asscoiation',
    sa.Column('ford_mustang_id', sa.INTEGER(), nullable=True),
    sa.Column('bid.id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['bid.id'], ['bids.id'], ),
    sa.ForeignKeyConstraint(['ford_mustang_id'], ['ford_mustangs.id'], name='fk_ford_mustang_bid_asscoiation_ford_mustang_id_ford_mustangs')
    )
    op.drop_table('ford_mustang_bid_association')
    # ### end Alembic commands ###
