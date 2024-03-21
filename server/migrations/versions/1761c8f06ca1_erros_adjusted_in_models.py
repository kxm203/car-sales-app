"""erros adjusted in models

Revision ID: 1761c8f06ca1
Revises: 
Create Date: 2024-03-21 14:38:04.065067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1761c8f06ca1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ford_mustangs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('bids',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_bids_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ford_mustang_bid_asscoiation',
    sa.Column('ford_mustang_id', sa.Integer(), nullable=True),
    sa.Column('bid.id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bid.id'], ['bids.id'], name=op.f('fk_ford_mustang_bid_asscoiation_bid.id_bids')),
    sa.ForeignKeyConstraint(['ford_mustang_id'], ['ford_mustangs.id'], name=op.f('fk_ford_mustang_bid_asscoiation_ford_mustang_id_ford_mustangs'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ford_mustang_bid_asscoiation')
    op.drop_table('bids')
    op.drop_table('users')
    op.drop_table('ford_mustangs')
    # ### end Alembic commands ###