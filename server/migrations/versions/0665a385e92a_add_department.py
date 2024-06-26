"""add Department

Revision ID: 0665a385e92a
Revises: 88c5836bb77b
Create Date: 2024-04-12 01:51:06.971227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0665a385e92a'
down_revision = '88c5836bb77b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
