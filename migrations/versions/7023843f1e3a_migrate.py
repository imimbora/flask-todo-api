"""'migrate'

Revision ID: 7023843f1e3a
Revises: 383eeefed4a7
Create Date: 2019-08-08 20:29:45.374740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7023843f1e3a'
down_revision = '383eeefed4a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_song',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('todo', sa.String(length=255), nullable=False),
    sa.Column('regdate', sa.DateTime(), nullable=False),
    sa.Column('complete', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_song')
    # ### end Alembic commands ###
