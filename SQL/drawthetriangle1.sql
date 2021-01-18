set @i = 21;
select repeat('* ', @i := @i - 1) FROM information_schema.tables 
