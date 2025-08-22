"""create freebies table

Revision ID: 05801cdff390
Revises: 5f72c58bf48c
Create Date: 2025-08-22 11:57:33.441679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05801cdff390'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_name', sa.String(length=255), nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('company_id', sa.Integer, nullable=False),
        sa.Column('dev_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['company_id'], ['companies.id']),
        sa.ForeignKeyConstraint(['dev_id'], ['devs.id'])
    )


def downgrade() -> None:
    op.drop_table("freebies")
