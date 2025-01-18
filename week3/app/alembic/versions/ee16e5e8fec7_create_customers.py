"""create customers

Revision ID: ee16e5e8fec7
Revises:
Create Date: 2025-01-17 23:06:16.972578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee16e5e8fec7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
      """
      CREATE TABLE customers(
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL
      );
      """
    )


def downgrade() -> None:
    op.execute(
      """
      DROP TABLE customers;
      """
    )
