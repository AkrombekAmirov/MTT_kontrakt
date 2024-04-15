"""initial migration

Revision ID: fe58ef880e93
Revises: 1841073e108a
Create Date: 2024-04-07 17:15:28.143207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe58ef880e93'
down_revision: Union[str, None] = '1841073e108a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
