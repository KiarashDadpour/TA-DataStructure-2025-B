def selection_sort(A):
    n = len(A)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if A[m_index] > A[j]:
                m_index = j
        A[m_index], A[i] = A[i], A[m_index]
    return A
