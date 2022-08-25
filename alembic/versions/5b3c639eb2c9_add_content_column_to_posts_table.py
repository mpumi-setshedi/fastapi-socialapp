"""add content column to posts table

Revision ID: 5b3c639eb2c9
Revises: 33b9dc6c9891
Create Date: 2022-08-23 14:09:01.050443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b3c639eb2c9'
down_revision = '33b9dc6c9891'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
