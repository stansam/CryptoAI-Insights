import React from 'react'

const VideoCard = ({ title, thumbnail, views, CGRating, channel, duration, description, dateUploaded }) => {
    return (
        <div>
            <h2 className='text-blue-500 text-2xl'>{channel.name}</h2>
            <div>
                <div>
                    <img src={`${thumbnail}`} alt="" />
                    <span>{duration}</span>
                </div>
                <h2>{title}</h2>
                <div>
                    <span>{views}</span>
                    <span>{dateUploaded}</span>
                </div>
                <div>
                    <span>{channel.name}</span>
                    <img src={`${channel.logo}`} alt="" />
                </div>
                <p>{description}</p>
            </div>
            <div>
                <span>Views: {views}</span>
                <span>Followers: {channel.followers}</span>
                <span>CryptoGopher Community rating: {CGRating} stars</span>
            </div>
        </div>
    )
}

export default VideoCard
