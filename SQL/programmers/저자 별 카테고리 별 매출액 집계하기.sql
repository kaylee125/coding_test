-- 오답
select a.AUTHOR_ID,
        a.AUTHOR_NAME,
        b.CATEGORY,
        sum(bs.sales*b.price) as TOTAL_SALES
from book b
inner join 
    (SELECT sum(sales) sales,book_id
    from book_sales
    group by book_id) bs
on b.book_id=bs.book_id
inner join author a 
on a.author_id=b.author_id
group by a.author_id
order by a.author_id ,b.category desc

-- 정답
--  결과 집합은 각 저자 및 카테고리 조합에 대해 하나의 행만 포함
select a.AUTHOR_ID,a.AUTHOR_NAME,b.CATEGORY,sum(bs.sales*b.price) as TOTAL_SALES
from book b
inner join book_sales bs on b.book_id=bs.book_id
inner join author a on a.author_id=b.author_id
where bs.sales_date BETWEEN '2022-01-01' AND '2022-01-31'
group by b.author_id,b.category
order by b.author_id ,b.category desc