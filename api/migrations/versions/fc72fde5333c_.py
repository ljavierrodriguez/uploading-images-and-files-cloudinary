"""empty message

Revision ID: fc72fde5333c
Revises: 51b0a3a4bcd6
Create Date: 2023-04-24 23:55:18.172759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc72fde5333c'
down_revision = '51b0a3a4bcd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('galleries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('galleries', schema=None) as batch_op:
        batch_op.drop_column('public_id')

    # ### end Alembic commands ###