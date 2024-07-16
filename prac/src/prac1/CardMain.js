// import React from 'react'
import { useState, useEffect, useRef } from "react";
import Card from "./Card";

export default function CardMain() {
    const [tdata, setTdata] = useState([]);
    const [tags, setTags] = useState([]);
    const inRef = useRef();
    
    const getData = (keyword) => {
        let url = 'https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?';
        url = url + `serviceKey=${process.env.REACT_APP_API_KEY}`;
        url = url + '&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A';
        url = url + `&keyword=${keyword}&_type=json`;
        console.log(url);

        fetch(url)
        .then(resp => resp.json())
        .then(data => setTdata(data.response.body.items.item))
        ;
    }

    //확인 버튼 클릭 시
    const handleClick = (e)=>{
        e.preventDefault();
        // inRef 변수에는 input 박스에 입력된 값이 할당됨.
        // inRef 변수의 현재값을 키워드로 지정한 뒤 getData 실행
        let keyword = encodeURI(inRef.current.value);
        
        // input 비었을 때 확인 누르면 오류남
        if (keyword == '') {
            alert('키워드를 입력하세요');
        }
        else {
            getData(keyword);
        }
    }

    //tdata 값이 변경되면 URL에서 가져온 값들로 tags 값 업데이트
    useEffect(()=>{
        let tm = tdata.map(item => <Card key={item.galContentId}
                                            galTitle = {item.galTitle}
                                            galWebImageUrl = {item.galWebImageUrl} />);
        setTags(tm);
    }, [tdata]);

    return (
        <div className='flex flex-col'>
            <form className="w-full flex m-5">
                <input type='text' id='txt1' 
                       ref={inRef}
                       className='placeholder="키워드 입력" text-gray-600'/>
                <button className='bg-gray-600 text-white text-lg p-5'
                        onClick={handleClick}>
                            확인</button>
            </form>
            <div className='h-full text-gray-600
                            grid grid-cols-1 gap-4
                            md:grid-cols-3'>
                {tags}
            </div>
        </div>
    )
}
