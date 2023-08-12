import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios';

const $axios: AxiosInstance = axios.create({
  baseURL: '/.netlify/functions',
  timeout: 10000, // 10 seconds
});

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(
    (response: AxiosResponse) => {
      return response;
    },
    (error: AxiosError) => {
      return Promise.reject(error);
    }
);


interface ResponseData {
  // specify the data type
}

export default {
  fetchRecords(): Promise<ResponseData> {
    return $axios.get<ResponseData>('airtable').then(response => {
      return response.data;
    });
  }
};
