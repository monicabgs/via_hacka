"""empty message

Revision ID: 5ae0da08a185
Revises: 
Create Date: 2020-11-16 11:29:23.609947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ae0da08a185'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_input',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_input', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('execution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('data_input', sa.String(), nullable=False),
    sa.Column('model_result', sa.String(), nullable=False),
    sa.Column('msg_status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('model_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_result', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('model_result')
    op.drop_table('execution')
    op.drop_table('data_input')
    # ### end Alembic commands ###