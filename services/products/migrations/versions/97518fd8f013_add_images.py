"""add images

Revision ID: 97518fd8f013
Revises: e9f42604f9a3
Create Date: 2022-11-18 00:00:37.996473

"""
import sqlmodel
import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '97518fd8f013'
down_revision = 'e9f42604f9a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column(
        'image', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'image')
    # ### end Alembic commands ###
