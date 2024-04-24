"""initial migration

Revision ID: 1841073e108a
Revises: 247144867f19
Create Date: 2024-04-07 17:14:50.715547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1841073e108a'
down_revision: Union[str, None] = '247144867f19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
