import {useCallback, useState} from 'react'
export const useHttp = () => {
    const [loading, setLoading] = useState (false)
    const [error, serError] = useState(null)

    // useCallback нужен, чтобы React не входил в рекурсию
    const request = useCallback(async (url, method='GET', body, headers={}) => {
        setLoading(true)


        try {
            if(body){
                body = JSON.stringify(body)
                headers['Content-Type'] = 'application/json'
            }

            const response = await fetch(url, {method, body, headers})
            const data = await response.json()

            setLoading(false)
            return data

        }catch (e) {
            console.log(e)
            setLoading(false)
            serError(e.message)
            throw e
        }
    }, [])

    const clearError = () => serError(null)

    return {loading, request, error, clearError}
}