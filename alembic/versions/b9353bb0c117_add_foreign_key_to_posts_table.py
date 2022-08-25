"""add foreign key to posts table

Revision ID: b9353bb0c117
Revises: 0b658619596a
Create Date: 2022-08-23 20:26:26.280281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9353bb0c117'
down_revision = '0b658619596a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users",
    local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
