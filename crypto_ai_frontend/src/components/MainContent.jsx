import React from 'react'
import videos from "./../MOCK_DATA/MOCK_VIDEOS"
import tokens from "./../MOCK_DATA/MOCK_TOKENS"
import VideoCard from './VideoCard'
import TokenCard from './TokenCard'

const MainContent = () => {

    return (
        <div className='flex'>
            <div>
                <span>Trending</span>
                {videos.map(({ title, thumbnail, views, followers, CGRating, channel, duration, description, dateUploaded }) => <VideoCard title={title} thumbnail={thumbnail} views={views} followers={followers} CGRating={CGRating} channel={channel} duration={duration} description={description} dateUploaded={dateUploaded} />)}
            </div>
            <div>
                <span>Tokens</span>
                <div>{tokens.map(({ image_url, currency }) => <TokenCard image_url={image_url} currency={currency} />)}</div>
            </div>
        </div>
    )
}

export default MainContent
