"""Had to rename image to image_url to match.

Revision ID: 43ae10b4b557
Revises: 5143b4f78aa7
Create Date: 2024-03-27 19:58:03.577879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43ae10b4b557'
down_revision = '5143b4f78aa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mustangs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(), nullable=True))
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mustangs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
