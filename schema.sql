CREATE TABLE IF NOT EXISTS Company (
  Ticker VARCHAR NOT NULL,
  Name VARCHAR,
  Exchange VARCHAR,
  Industry VARCHAR,
  Sector VARCHAR,
  PRIMARY KEY (Ticker)
);

CREATE TABLE IF NOT EXISTS PriceVolume (
  Ticker VARCHAR NOT NULL,
  Day Date NOT NULL,
  OpenPrice FLOAT,
  ClosePrice FLOAT,
  AdjustedClosePrice FLOAT,
  HighPrice FLOAT,
  LowPrice FLOAT,
  Volume FLOAT,
  PRIMARY KEY (Ticker, Day),
  FOREIGN KEY (Ticker) REFERENCES Company (Ticker)
);
