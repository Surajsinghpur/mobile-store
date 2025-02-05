"""Fix mobile model

Revision ID: 3a8a41472759
Revises: 
Create Date: 2024-12-23 15:20:45.280142

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a8a41472759'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mobiles')
    op.drop_table('bookings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mobile_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('customer_address', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('delivery_date', sa.DATE(), nullable=False),
    sa.ForeignKeyConstraint(['mobile_id'], ['mobiles.id'], name='bookings_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('mobiles',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('price', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('details', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
