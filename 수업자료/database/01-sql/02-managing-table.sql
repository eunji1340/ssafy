-- Table 구조 확인
PRAGMA table_info('examples');
PRAGMA table_info('new_examples');

-- 1. Create a table
CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

-- 2. Modifying table fields
-- 2.1 ADD COLUMN
ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT 'default value';

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음
-- ALTER TABLE
--   examples
-- ADD COLUMN
--   sampleCol1 VARCHAR(100) NOT NULL DEFAULT 'default value'
-- ADD COLUMN
--   sampleCol2 VARCHAR(100) NOT NULL DEFAULT 'default value';

ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL DEFAULT 0;


ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL DEFAULT 'default value';


-- 2.2 RENAME COLUMN
ALTER TABLE
  examples
RENAME COLUMN
  Address TO Postcode;

-- 2.3 DROP COLUMN
ALTER TABLE
  examples
DROP COLUMN
  PostCode;

-- 2.4 RENAME TO
ALTER TABLE
  examples
RENAME TO
  new_examples;

-- 3. Delete a table
DROP TABLE new_examples;


-- sqlite는 컬럼 수정(데이터 타입, 제약조건 등) 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
