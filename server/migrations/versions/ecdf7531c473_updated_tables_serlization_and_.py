"""updated tables serlization and association proxy

Revision ID: ecdf7531c473
Revises: a01005978e38
Create Date: 2024-04-17 11:46:11.974563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecdf7531c473'
down_revision = 'a01005978e38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_review_customer_id_customers')),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_review_item_id_items')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reviews')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('comment', sa.VARCHAR(), nullable=True),
    sa.Column('customer_id', sa.INTEGER(), nullable=True),
    sa.Column('iteam_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='fk_reviews_customer_id_customers'),
    sa.ForeignKeyConstraint(['iteam_id'], ['items.id'], name='fk_reviews_iteam_id_items'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('review')
    # ### end Alembic commands ###
