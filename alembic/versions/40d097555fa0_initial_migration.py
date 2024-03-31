"""Initial migration

Revision ID: 40d097555fa0
Revises: 
Create Date: 2024-03-31 11:43:07.108720

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40d097555fa0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('filechunk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('chunk', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_filechunk_id'), 'filechunk', ['id'], unique=False)
    op.create_table('filerepository',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('contract_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('content_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('time', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_filerepository_id'), 'filerepository', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('passport', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('telegram_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('telegram_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('contract_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('telegram_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('faculty', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('group', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_created_date'), 'user', ['created_date'], unique=False)
    op.create_index(op.f('ix_user_created_time'), 'user', ['created_time'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_created_time'), table_name='user')
    op.drop_index(op.f('ix_user_created_date'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_filerepository_id'), table_name='filerepository')
    op.drop_table('filerepository')
    op.drop_index(op.f('ix_filechunk_id'), table_name='filechunk')
    op.drop_table('filechunk')
    # ### end Alembic commands ###
