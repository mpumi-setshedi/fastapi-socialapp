"""add user table

Revision ID: 0b658619596a
Revises: 5b3c639eb2c9
Create Date: 2022-08-23 20:05:56.408238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b658619596a'
down_revision = '5b3c639eb2c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), nullable=False),

    sa.Column("email", sa.String(), nullable=False),

    sa.Column("password", sa.String(), nullable=False),

    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),

    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email"))

    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
