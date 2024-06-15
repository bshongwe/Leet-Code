#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;

    /* setting the size of the return array to 2 */
    *returnSize = 2;

    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                /* allocate memory for the result array */
                int* res = (int*)malloc(sizeof(int) * 2);
                if (res == NULL) {
		    /* memory allocation failed */
                    *returnSize = 0;
                    return NULL;
                }
		/**
		 * store the 1st and 2nd index,
		 * return result array
		 */
                res[0] = i;
                res[1] = j;
                return res;
            }
        }
    }
    
    /**
     * if no solution found, set return size to 0,
     * else, return NULL
     */
    *returnSize = 0;
    return NULL;
}
