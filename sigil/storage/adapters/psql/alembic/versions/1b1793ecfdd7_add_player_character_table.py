"""Add player character table

Revision ID: 1b1793ecfdd7
Revises: 7c347be1029f
Create Date: 2022-04-30 22:37:17.590917

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1b1793ecfdd7"
down_revision = "7c347be1029f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "player_characters",
        sa.Column("uuid", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("notes", sa.TEXT(), nullable=True),
        sa.Column("player", sa.String(), nullable=True),
        sa.Column("uri", sa.String(), nullable=True),
        sa.Column("campaign_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["campaign_id"],
            ["campaigns.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("player_characters")
    # ### end Alembic commands ###
