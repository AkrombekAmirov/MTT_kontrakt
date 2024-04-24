"""initial migration

Revision ID: 247144867f19
Revises: 95d84fa5d9ed
Create Date: 2024-04-07 15:58:21.610383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '247144867f19'
down_revision: Union[str, None] = '95d84fa5d9ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
