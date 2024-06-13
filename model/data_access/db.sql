create database library;

-- Book
create table library.books
(
    id        int primary key auto_increment,
    isbn      int not null,
    title     nvarchar(30) not null,
    author    nvarchar(30),
    language  nvarchar(30),
    pubdate   date
);

-- Member
create table library.members
(
    id         int primary key auto_increment,
    name       nvarchar(30) not null,
    role       nvarchar(15) not null,
    email      nvarchar(30),
    phone      nvarchar(11) not null unique,
    join_date  date
);

-- Loan
create table library.loans
(
    loan_id    int primary key auto_increment,
    book_id    int not null,
    member_id  int not null,
    loan_date  date,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

create view library.loaned_books_count as
select member_id, count(member_id) as count_loaned_books from library.loans
group by member_id;
