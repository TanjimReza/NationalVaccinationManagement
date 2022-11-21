"""empty message

Revision ID: a5229c0fcf73
Revises: 
Create Date: 2022-11-18 19:57:40.916675

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a5229c0fcf73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_type', sa.String(length=100), nullable=True))
        batch_op.drop_column('is_hospital')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_hospital', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.drop_column('user_type')

    # ### end Alembic commands ###