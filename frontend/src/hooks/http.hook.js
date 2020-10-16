import {useCallback, useState} from 'react'
export const useHttp = () => {
    const [loading, setLoading] = useState (false)
    const request = useCallback(async (url, method='GET', body = null, headers={}) => {
        setLoading(true)
        try {
            const response = await fetch(url, {method, body, headers})
            const data = await response.json()

            setLoading(false)
            return data

        }catch (e) {
            setLoading(false)
            throw e
        }
    }, [])

    return {loading, request}
}