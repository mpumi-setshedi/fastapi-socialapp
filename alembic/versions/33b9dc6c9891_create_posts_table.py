"""create posts table

Revision ID: 33b9dc6c9891
Revises: 
Create Date: 2022-08-20 12:14:34.951758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33b9dc6c9891'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass