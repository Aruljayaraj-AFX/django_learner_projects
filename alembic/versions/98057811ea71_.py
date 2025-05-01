"""empty message

Revision ID: 98057811ea71
Revises: 3832a78f6a9d
Create Date: 2025-05-01 13:16:21.394828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98057811ea71'
down_revision: Union[str, None] = '3832a78f6a9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
