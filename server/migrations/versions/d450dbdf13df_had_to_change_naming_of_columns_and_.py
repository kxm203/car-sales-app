"""Had to change naming of columns and added bid_amount validation.

Revision ID: d450dbdf13df
Revises: f1595716cf76
Create Date: 2024-03-26 19:06:41.114617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd450dbdf13df'
down_revision = 'f1595716cf76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bids', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.create_unique_constraint('bids', ['username'])
        batch_op.drop_column('user_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bids', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_name', sa.VARCHAR(), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###