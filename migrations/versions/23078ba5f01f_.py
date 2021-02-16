"""empty message

Revision ID: 23078ba5f01f
Revises: 09df00b29a8e
Create Date: 2021-02-15 18:12:57.361317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23078ba5f01f'
down_revision = '09df00b29a8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('update_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'update_at')
    op.drop_column('user', 'create_at')
    # ### end Alembic commands ###