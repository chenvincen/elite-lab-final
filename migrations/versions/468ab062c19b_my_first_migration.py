"""my first migration

Revision ID: 468ab062c19b
Revises: 
Create Date: 2020-11-04 18:49:34.483308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '468ab062c19b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('hash_key', sa.String(length=6), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash_key')
    )
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=16), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_session_token'), 'session', ['token'], unique=True)
    op.create_index(op.f('ix_session_username'), 'session', ['username'], unique=False)
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_chat_id'), 'message', ['chat_id'], unique=False)
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    op.create_index(op.f('ix_message_username'), 'message', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_username'), table_name='message')
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_index(op.f('ix_message_chat_id'), table_name='message')
    op.drop_table('message')
    op.drop_index(op.f('ix_session_username'), table_name='session')
    op.drop_index(op.f('ix_session_token'), table_name='session')
    op.drop_table('session')
    op.drop_table('chat')
    # ### end Alembic commands ###
