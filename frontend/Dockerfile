FROM node:20

WORKDIR /app

# Copy package files first
COPY package*.json ./

# Clean install with platform-specific binaries
RUN rm -rf node_modules package-lock.json
RUN npm install

# Copy the rest of your frontend code
COPY . .

# Expose Vite's port
EXPOSE 5173

# Run Vite dev server
CMD ["npm", "run", "dev"]