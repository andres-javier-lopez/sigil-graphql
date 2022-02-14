"""campaign table

Revision ID: 509455681492
Revises:
Create Date: 2022-02-14 21:36:21.575693

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '509455681492'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('campaings',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('notes', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )


def downgrade():
    op.drop_table('campaings')
