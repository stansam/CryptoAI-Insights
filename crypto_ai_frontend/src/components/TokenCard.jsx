import React from 'react'

const TokenCard = ({image_url, currency}) => {
    return (
        <div>
            <img src={`${image_url}`} alt="" />
            <span>Entry: ${currency}</span>
        </div>
    )
}

export default TokenCard
