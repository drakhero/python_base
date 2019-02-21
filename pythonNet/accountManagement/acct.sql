create table acct(
    acct_no varchar(32) primary key,
    acct_name varchar(64) not null,
    reg_date date,
    acct_type int,
    balance decimal(18,2)
);
insert into acct values(
    '622345000002','Tom',now(),1,2000.00
);