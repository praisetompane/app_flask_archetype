"""create table computation_result

Revision ID: f7950a5c213d
Revises: 9e2772c6755f
Create Date: 2025-02-10 13:51:24.494766

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f7950a5c213d"
down_revision: Union[str, None] = "9e2772c6755f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        sa.DDL(
            """
            CREATE TABLE IF NOT EXISTS computation.computation_result
            (
                "Id" int4 NULL,
                "IndicatorCode" varchar(20) NULL,
                "SpatialDimType" varchar(10) NULL,
                "SpatialDim" varchar(10) NULL,
                "ParentLocationCode" varchar(10) NULL,
                "ParentLocation" varchar(50) NULL,
                "TimeDimType" varchar(20) NULL,
                "TimeDim" int4 NULL,
                "Dim1Type" varchar(50) NULL,
                "Dim1" varchar(50) NULL,
                "Dim2Type" varchar(50) NULL,
                "Dim2" varchar(50) NULL,
                "Dim3Type" varchar(50) NULL,
                "Dim3" varchar(50) NULL,
                "DataSourceDimType" varchar(50) NULL,
                "DataSourceDim" varchar(50) NULL,
                "Value" varchar(50) NULL,
                "NumericValue" int4 NULL,
                "Low" varchar(50) NULL,
                "High" varchar(50) NULL,
                "Comments" varchar(100) NULL,
                "Date" timestamp NULL,
                "TimeDimensionValue" varchar(10) NULL,
                "TimeDimensionBegin" timestamp NULL,
                "TimeDimensionEnd" timestamp NULL
            );
        """
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        sa.DDL("DROP TABLE IF EXISTS computation.computation_result;")
    )
