"""New Migration

Revision ID: 9a9c3550acc9
Revises: ac099c944041
Create Date: 2023-02-10 13:03:05.357794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a9c3550acc9'
down_revision = 'ac099c944041'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_city_id'), 'city', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_city_id'), table_name='city')
    # ### end Alembic commands ###
