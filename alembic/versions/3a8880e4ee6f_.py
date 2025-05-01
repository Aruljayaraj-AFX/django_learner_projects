"""empty message

Revision ID: 3a8880e4ee6f
Revises: 98057811ea71
Create Date: 2025-05-01 13:20:37.051428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a8880e4ee6f'
down_revision: Union[str, None] = '98057811ea71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
