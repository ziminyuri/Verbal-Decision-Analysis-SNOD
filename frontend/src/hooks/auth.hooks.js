import {useState, useCallback, useEffect} from 'react'

const storageName = 'userData'

export const useAuth = () => {
    const [token, setToken] = useState(null)
    const [userId, setUserid] = useState(null)

    const login = useCallback((jwtToken, id) => {
        setToken(jwtToken)
        setUserid(id)

        localStorage.setItem(storageName, JSON.stringify({
            userId: id, token: jwtToken
        }))
    }, [])
    const logout = useCallback(() => {
        setToken(null)
        setUserid(null)
        localStorage.removeItem(storageName)
    }, [])


    useEffect(() => {
        const data = JSON.parse(localStorage.getItem(storageName))

        if (data && data.token){
            login(data.token, data.user_id)
        }
    }, [login])

    return {login, logout, token, userId}
}