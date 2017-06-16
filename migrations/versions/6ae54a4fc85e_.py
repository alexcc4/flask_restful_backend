"""empty message

Revision ID: 6ae54a4fc85e
Revises: 5918c8f886f9
Create Date: 2017-06-07 17:40:38.481785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ae54a4fc85e'
down_revision = '5918c8f886f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.Column('email', sa.String(length=256), nullable=True),
                    sa.Column('password_hash', sa.String(length=256), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foos')
    op.drop_table('accounts')
    # ### end Alembic commands ###
