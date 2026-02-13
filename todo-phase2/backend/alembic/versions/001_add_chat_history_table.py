"""Add chat_history table

Revision ID: 001_add_chat_history_table
Revises:
Create Date: 2026-02-03 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
import uuid
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '001_add_chat_history_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the chat_history table
    op.create_table(
        'chathistory',
        sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column('session_id', sa.VARCHAR(length=255), nullable=False),
        sa.Column('role', sa.VARCHAR(length=20), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create indexes for efficient querying
    op.create_index('idx_chathistory_session_created', 'chathistory', ['session_id', 'created_at'])
    op.create_index('idx_chathistory_session_role', 'chathistory', ['session_id', 'role'])


def downgrade():
    # Drop the chat_history table and its indexes
    op.drop_index('idx_chathistory_session_created', table_name='chathistory')
    op.drop_index('idx_chathistory_session_role', table_name='chathistory')
    op.drop_table('chathistory')