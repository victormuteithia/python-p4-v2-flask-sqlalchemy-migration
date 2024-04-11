"""rename department

Revision ID: 634519688c8f
Revises: 0665a385e92a
Create Date: 2024-04-12 02:07:36.474818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '634519688c8f'
down_revision = '0665a385e92a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
