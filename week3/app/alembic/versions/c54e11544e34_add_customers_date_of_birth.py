"""add customers date_of_birth

Revision ID: c54e11544e34
Revises: ee16e5e8fec7
Create Date: 2025-01-17 23:11:55.008732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c54e11544e34'
down_revision: Union[str, None] = 'ee16e5e8fec7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
      """
      ALTER TABLE customers
      ADD COLUMN date_of_birth TIMESTAMP;
      """
    )


def downgrade():
    op.execute(
      """
      ALTER TABLE customers
      DROP COLUMN date_of_birth;
      """
    )
