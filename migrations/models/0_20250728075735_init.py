from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "ingcategorymodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "usermodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(100) NOT NULL,
    "name" VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "ingredientmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "quantity" DOUBLE PRECISION NOT NULL,
    "unit" VARCHAR(20) NOT NULL,
    "expiry_date" DATE NOT NULL,
    "stored_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "category_id" INT NOT NULL REFERENCES "ingcategorymodel" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "usermodel" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
