"""initial migration

Revision ID: 95d84fa5d9ed
Revises: 40d097555fa0
Create Date: 2024-04-07 12:23:18.997339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95d84fa5d9ed'
down_revision: Union[str, None] = '40d097555fa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
