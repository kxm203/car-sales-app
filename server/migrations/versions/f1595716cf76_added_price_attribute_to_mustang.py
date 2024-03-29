"""added price attribute to Mustang

Revision ID: f1595716cf76
Revises: d00f4c4e0498
Create Date: 2024-03-26 16:36:01.485250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1595716cf76'
down_revision = 'd00f4c4e0498'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mustangs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mustangs', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###
